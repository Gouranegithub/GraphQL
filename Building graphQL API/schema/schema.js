const graphql= require('graphql');
const _ = require('lodash');
const{GraphQLObjectType,
     GraphQLString,
     GraphQLInt,
     GraphQLSchema} = graphql

const users = [
    {"id":"23", "firstName":"Bill", "age":20},
    {"id":"24", "firstName":"Alice", "age":22},
    {"id":"25", "firstName":"John", "age":25},
    {"id":"26", "firstName":"Emma", "age":28},
    {"id":"27", "firstName":"Mike", "age":21},
    {"id":"28", "firstName":"Sophia", "age":24},
    {"id":"29", "firstName":"James", "age":23},
    {"id":"30", "firstName":"Olivia", "age":26},
    {"id":"31", "firstName":"Henry", "age":27},
    {"id":"32", "firstName":"Mia", "age":29}
];

const UserType = new GraphQLObjectType({
    name: 'User',
    fields:{
        id:{type: GraphQLString},
        firstName:{type: GraphQLString},
        age:{type: graphql.GraphQLInt}
    }
})


const RootQuery = new GraphQLObjectType({
    name:'RootQueryType',
    fields:{
        user:{
            type: UserType,
            args:{id:{type: GraphQLString}},
            resolve(parentValue, args){
                return _.find(users,{id: args.id})
            }

        }
    }
})

module.exports= new graphql.GraphQLSchema({
    query:RootQuery
})