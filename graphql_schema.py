import graphene

class Todo(graphene.ObjectType):
    id = graphene.Int(required=True)
    title = graphene.String(required=True)
    description = graphene.String()
    time = graphene.DateTime()
    images = graphene.List(graphene.String)  # Accessible only with Pro license

class TodoInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String()
    time = graphene.DateTime()

class Mutation(graphene.ObjectType):
    create_todo = graphene.Field(Todo, input=TodoInput, requires_auth=True)
    update_todo = graphene.Field(Todo, id=graphene.Int(required=True), input=TodoInput, requires_auth=True)
    delete_todo = graphene.Field(graphene.Boolean, id=graphene.Int(required=True), requires_auth=True)

    def resolve_create_todo(self, context, input):
        # to create a todo with user ID and Pro license check
        pass

    def resolve_update_todo(self, context, id, input):
        # to update a todo
        pass

    def resolve_delete_todo(self, context, id):
        # to delete a todo
        pass

class Query(graphene.ObjectType):
    todos = graphene.List(Todo, requires_auth=True)

    def resolve_todos(self, context):
        # to retrieve
