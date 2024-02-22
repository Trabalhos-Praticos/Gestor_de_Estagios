describe('api test', () => {
    it('GET - all users', () => {
           
    cy.api('/api/users');
    });
})
