describe('api test', () => {
    it('GET - all users', () => {
           
        cy.request({
            method: 'GET',
            url: '/api/users/',
            headers: {
              'Accept': 'application/json'
            }
          }).then((response) => {
            expect(response.status).to.eq(200);
            expect(response.body).to.be.an('array');
          });
          
    });
})
