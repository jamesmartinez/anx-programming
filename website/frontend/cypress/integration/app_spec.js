describe("irclog submission", () => {

  const irclog = {
    nick: "slowjames",
    message: "im a cute girl"
  };

  before(() => {
    cy.exec("npm run dev");
    cy.exec("npm run flush");
  });

  it("should be able to fill a web form", () => {
    cy.visit("/");
    cy
      .get('input[name="nick"]')
      .type(irclog.nick)
      .should("have.value", irclog.nick);
    cy
      .get('textarea[name="message"]')
      .type(irclog.message)
      .should("have.value", irclog.message);

      cy.get("form").submit();
  });
   
	it("should be able to see the table", () => {
      cy.visit("/");
      cy.get("tr").contains(`${irclog.nick}${irclog.message}`);
    });
});
