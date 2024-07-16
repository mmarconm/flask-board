/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{html,js}"],
  theme: ["bumblebee", "light"],
  plugins: [require("daisyui")],
};
