# Significance of URL redirection

'''
    1. Reorganization: If you are reorganizing your website's structure or change the URL of a page, redirection helps maintain backward compatability for the users who might have bookmarked or accessed the old url

    2. Content migration: If you are moving content from one URL to another, redirection allows you to maintain the old URL for SEO and user experience while redirecting the content to the new URL

    3. SEO: Redirection is important for SEO (Search Engine Optimization) as it helps search engines understand the new URL and index the content correctly

    4. Security: Redirection can be used to protect sensitive information or resources from unauthorized access

    5. Accessibility: Redirection can help make content more accessible to users who may not be able to access the original URL

    6. User experience: Redirection can improve user experience by providing a smooth transition between old and new URLs

'''

from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Home page</p>"

# Define a route for '/page-1'
@app.route('/page-1')
def page_1():
    # Redirect to '/page-2' with a 302 status code (temporary redirect)
    return redirect(url_for('page_2'), code=302)

# Define a route for '/page-2'
@app.route('/page-2')
def page_2():
    # Render the 'page-2.html' template
    return render_template('./page-2.html')

# Define a route for '/about'
@app.route('/about')
def about():
    return '<p>About page</p>'

# Define a route for '/contact'
@app.route('/contact')
def contact():
    return '<p>Contact page</p>'

# Run the app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000, debug=True)
