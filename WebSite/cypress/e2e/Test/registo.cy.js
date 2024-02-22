/// <reference types="cypress" />
context('Realizar um Registo', () => {
    beforeEach(() => {
      cy.visit('http://127.0.0.1:8000')
    })
    it('Fazer Registo', () => {
      cy.get('#registoBtn').click()
      cy.get('#pnome').type('Ines').should('have.value', 'Ines')
      cy.get('#unome').type('Cunha').should('have.value','Cunha')
      cy.get('#email').type('inescunha@ipvc.pt').should('have.value','inescunha@ipvc.pt')
      cy.get('#password').type('Ines123#').should('have.value','Ines123#')
      cy.get('#confirm-password').type('Ines123#').should('have.value','Ines123#')
      cy.get('#countries').select('Construção e Reabilitação')
      cy.get('form').submit()
    });
})