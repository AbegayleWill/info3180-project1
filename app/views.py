"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for

from flask import flash, session, abort, send_from_directory

from app.forms import PropertyForm
from app import db
from app.models import Property
import os
from werkzeug.utils import secure_filename
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Abegayle Williams")

@app.route('/property/', methods=['GET', 'POST'])
def new_property():
    # Loads up the form
    property_form = PropertyForm()

    # Checks for method type and validatation
    if request.method == 'POST':
        if property_form.validate_on_submit():

            # Collect the data from the form
            p_title = property_form.p_title.data
            description = property_form.p_description.data
            rooms = property_form.rooms.data
            bathrooms = property_form.bathrooms.data
            price = property_form.price.data
            p_type = property_form.p_type.data
            location = property_form.location.data

            photo = property_form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Create a Property object
            my_property = Property(p_title, description, rooms, bathrooms, price, p_type, location, filename)
            db.session.add(my_property)
            db.session.commit()

            # Redirects user to the Properties page
            flash('Property Added Successfully!', 'success')
            return redirect(url_for('all_properties'))
    else:
        flash_errors(property_form)

    return render_template('property.html', form=property_form)


@app.route('/properties/')
def all_properties():
    properties = Property.query.all()

    return render_template('properties.html', properties=properties)


@app.route('/property/<property_id>')
def specific_property(property_id):
    property_id = int(property_id)

    # Locates the Property with the matching ID
    my_property = Property.query.filter_by(id=property_id).first()

    return render_template('single_property.html', property=my_property)

@app.route('/uploads/<filename>')
def get_uploaded_images(filename):
    rootdir = os.getcwd()
    return  send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
