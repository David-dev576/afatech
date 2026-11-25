/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        midnight: '#0F2942',
        'midnight-700': '#1A3A5C',
        royal: '#2563EB',
        'royal-600': '#1D4ED8', // Ajouté pour le hover
        icy: '#F4F7FA',
        slate: '#1E293B',
        mist: '#CBD5E1', // Ajouté (c'était 'borderblue' avant, on harmonise)
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'sans-serif'], // Alias pour les titres
        heading: ['"Space Grotesk"', 'sans-serif'], // Alias principal
        body: ['"Source Sans 3"', 'sans-serif'],
      }
    },
  },
  plugins: [],
}