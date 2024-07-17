const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const port = 4800;
const app = express();
const schema= require('./schema/schema');

app.use('/graphql',graphqlHTTP({
    schema,
    graphiql:true
}) )

app.listen(port, () => {
    console.log(`listing to port ${port}`)
})
