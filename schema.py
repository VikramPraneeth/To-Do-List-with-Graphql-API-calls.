from flask_graphql import GraphQLView

from .models import Todo
from .resolvers import resolvers

schema = build_schema(
    query=Query,
    mutation=Mutation,
    resolvers=resolvers
)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema))
