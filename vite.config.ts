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
          diensten: path.resolve(__dirname, 'diensten/index.html'),
          groepenkast: path.resolve(__dirname, 'groepenkast/index.html'),
          perilex: path.resolve(__dirname, 'perilex/index.html'),
          laadpaal: path.resolve(__dirname, 'laadpaal-installeren/index.html'),
          krachtstroom: path.resolve(__dirname, 'krachtstroom-aanleggen/index.html'),
          frezen: path.resolve(__dirname, 'frezen-stopcontacten-verleggen/index.html'),
          tuinverlichting: path.resolve(__dirname, 'tuinverlichting-buitenelektra/index.html'),
          spoed: path.resolve(__dirname, 'spoed-elektricien-utrecht/index.html'),
          tarieven: path.resolve(__dirname, 'tarieven/index.html'),
          werkwijze: path.resolve(__dirname, 'werkwijze/index.html'),
          werkgebied: path.resolve(__dirname, 'werkgebied/index.html'),
          wijken: path.resolve(__dirname, 'wijken/index.html'),
          vakmanschap: path.resolve(__dirname, 'vakmanschap/index.html'),
          reviews: path.resolve(__dirname, 'reviews/index.html'),
          offerte: path.resolve(__dirname, 'offerte/index.html'),
          afspraak: path.resolve(__dirname, 'afspraak/index.html'),
          faq: path.resolve(__dirname, 'faq/index.html'),
          contact: path.resolve(__dirname, 'contact/index.html'),
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
