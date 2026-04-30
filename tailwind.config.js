/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./en/*.html",
  ],
  theme: {
    extend: {
      colors: {
        navy: { DEFAULT: '#1a120b', dark: '#120c06', mid: '#2a1f14', light: '#3d3024' },
        gold: { DEFAULT: '#F7CD6F', dark: '#d4a843', light: '#fbe4a8' },
        cream: { DEFAULT: '#f5f0e8', muted: '#a89f8c' },
      },
      fontFamily: {
        serif: ['"EB Garamond"', 'Georgia', 'serif'],
        sans: ['"DM Sans"', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
