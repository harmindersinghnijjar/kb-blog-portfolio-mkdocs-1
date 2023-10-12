/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.html', // If you have any HTML files inside of src/ folder
    './docs/**/*.md', // If you have any Markdown files
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

