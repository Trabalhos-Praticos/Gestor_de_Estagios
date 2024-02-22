/// <reference types="cypress" />
context('Teste basico', () => {
  beforeEach(() => {
    cy.session('userSession', () => {
      cy.visit('http://127.0.0.1:8000');
      cy.get('#loginBtn').click();
      cy.get('#email').type('andre.c@ipvc.pt').should('have.value', 'andre.c@ipvc.pt');
      cy.get('#password').type('Andre1gpg').should('have.value','Andre1gpg');
      cy.get('form').submit();
    });
  });
    it('Fazer logout', () => {
      cy.visit('http://127.0.0.1:8000/dashboard');
      cy.get('#dropdownUserAvatarButton').click()
      cy.get('#logoutBtn').click()
    });
})
  
