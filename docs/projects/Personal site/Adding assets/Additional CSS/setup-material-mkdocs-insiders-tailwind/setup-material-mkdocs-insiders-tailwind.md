# Integrating Tailwind CSS with Material for MkDocs Insiders

Follow this step-by-step guide to seamlessly integrate Tailwind CSS with Material for MkDocs Insiders.

## Setting Up Material for MkDocs

Ensure that you have set up Material for MkDocs following their official documentation.

## Install Tailwind CSS

Navigate to your MkDocs project directory and execute:

    npm install tailwindcss postcss autoprefixer

## Setting up PostCSS and Tailwind

Create a `postcss.config.js` in your project root with:

    module.exports = {
      plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
      ],
    }

Next, initialize a Tailwind configuration:

    npx tailwindcss init

## Create Your Custom CSS File

Inside `docs/stylesheets/`, create `tailwind.css` and add:

    @import 'tailwindcss/base';
    @import 'tailwindcss/components';
    @import 'tailwindcss/utilities';

## Build Tailwind CSS

Execute the following:

    npx tailwindcss build docs/stylesheets/tailwind.css -o docs/stylesheets/output.css

## Update MkDocs Configuration

Edit your `mkdocs.yml`:

    extra_css:
      - stylesheets/output.css

## Customization

You can now utilize Tailwind's utility classes in your Markdown or any custom HTML in your documentation.

## Build MkDocs

Finally, build your MkDocs project with:

    mkdocs build

Note: Any changes made to Tailwind or your custom CSS require you to rebuild Tailwind CSS and then rebuild your MkDocs project.
