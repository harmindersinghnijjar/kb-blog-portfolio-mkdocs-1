---
title: Integrating Tailwind CSS with Material for MkDocs Insiders
description: Combine the power of Tailwind CSS with Material for MkDocs Insiders to create a documentation site that not only has the robust features and beautiful design of Material but also the utility-first flexibility and customization of Tailwind CSS.
authors: [harmindersinghnijjar]
date: 2023-11-05
tags: [Tailwind CSS, Material for MkDocs, MkDocs, CSS, Web Development]
toc: true
permalink: /projects/Personal-site/Adding-assets/Additional-CSS/setup-material-mkdocs-insiders-tailwind/
comments: true


---

# Integrating Tailwind CSS with Material for MkDocs Insiders

## Introduction

Combine the power of Tailwind CSS with Material for MkDocs Insiders to create a documentation site that not only has the robust features and beautiful design of Material but also the utility-first flexibility and customization of Tailwind CSS. This guide will walk you through the steps to integrate Tailwind CSS into your MkDocs project, allowing you to tailor the look and feel of your site with ease.

## Setting Up Material for MkDocs

Start by setting up Material for MkDocs as per the official guidelines. Ensure you have a running MkDocs environment before proceeding with the integration of Tailwind CSS.

## Install Tailwind CSS

Within your MkDocs project directory, run the following command to install the necessary packages:

```bash
npm install tailwindcss postcss autoprefixer
```

These packages include Tailwind CSS for the utility-first CSS framework, PostCSS for processing CSS with JavaScript, and Autoprefixer for handling CSS vendor prefixes.

## Setting up PostCSS and Tailwind

Create a `postcss.config.js` file in the root of your MkDocs project with the following content:

```javascript
module.exports = {
  plugins: [require('tailwindcss'), require('autoprefixer')]
}
```

Then, initialize your Tailwind configuration file which Tailwind uses to read your customization settings:

```bash
npx tailwindcss init
```

## Create Your Custom CSS File

Make a new CSS file in the `docs/stylesheets/` directory named `tailwind.css`. This file will import Tailwind's layers for you to use throughout your project:

```css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
```

## Build Tailwind CSS

Compile your CSS with Tailwind's styles by running:

```bash
npx tailwindcss build docs/stylesheets/tailwind.css -o docs/stylesheets/output.css
```

This command will process your custom CSS file and output a fully compiled CSS file with all of Tailwind's utility classes.

## Update MkDocs Configuration

Include the compiled CSS in your MkDocs configuration by editing `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/output.css
```

## Customization

You can now use Tailwind CSS classes in your Markdown content or in any HTML templates you're using within your MkDocs site.

## Build MkDocs

To see the changes take effect, build your MkDocs project with:

    mkdocs build

Note: Any changes made to Tailwind or your custom CSS require you to rebuild Tailwind CSS and then rebuild your MkDocs project.
