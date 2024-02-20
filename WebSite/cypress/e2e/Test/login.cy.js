/// <reference types="cypress" />
context('Realizar um Login', () => {
    beforeEach(() => {
      cy.visit('http://127.0.0.1:8000')
    })
    it('Fazer Login', () => {
      cy.get('#loginBtn').click()
      cy.get('#email').type('andre.c@ipvc.pt').should('have.value', 'andre.c@ipvc.pt')
      cy.get('#password').type('Andre1gpg').should('have.value','Andre1gpg')
      cy.get('#loginBtn').click()
    });
})
