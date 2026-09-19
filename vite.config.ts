import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig} from 'vite';

export default defineConfig(() => {
  return {
    plugins: [react(), tailwindcss()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    build: {
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, 'index.html'),
          diensten: path.resolve(__dirname, 'diensten.html'),
          groepenkast: path.resolve(__dirname, 'groepenkast.html'),
          perilex: path.resolve(__dirname, 'perilex.html'),
          laadpaal: path.resolve(__dirname, 'laadpaal-installeren.html'),
          krachtstroom: path.resolve(__dirname, 'krachtstroom-aanleggen.html'),
          frezen: path.resolve(__dirname, 'frezen-stopcontacten-verleggen.html'),
          tuinverlichting: path.resolve(__dirname, 'tuinverlichting-buitenelektra.html'),
          spoed: path.resolve(__dirname, 'spoed-elektricien-utrecht.html'),
          tarieven: path.resolve(__dirname, 'tarieven.html'),
          werkwijze: path.resolve(__dirname, 'werkwijze.html'),
          werkgebied: path.resolve(__dirname, 'werkgebied.html'),
          wijken: path.resolve(__dirname, 'wijken.html'),
          vakmanschap: path.resolve(__dirname, 'vakmanschap.html'),
          reviews: path.resolve(__dirname, 'reviews.html'),
          offerte: path.resolve(__dirname, 'offerte.html'),
          afspraak: path.resolve(__dirname, 'afspraak.html'),
          faq: path.resolve(__dirname, 'faq.html'),
          contact: path.resolve(__dirname, 'contact.html'),
        },
      },
    },
    server: {
      // HMR is disabled in AI Studio via DISABLE_HMR env var.
      // Do not modifyâfile watching is disabled to prevent flickering during agent edits.
      hmr: process.env.DISABLE_HMR !== 'true',
      // Disable file watching when DISABLE_HMR is true to save CPU during agent edits.
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});
