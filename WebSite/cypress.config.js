const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://127.0.0.1:8000', // Coloque baseUrl diretamente sob e2e
    setupNodeEvents(on, config) {
      // Implemente os listeners de eventos do Node aqui, se necessário
    },
  }
});
