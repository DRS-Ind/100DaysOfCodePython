from credentials import user_token, username, graph_id
from user import PixelaUser
from graph import GraphPixela


if __name__ == '__main__':
    user = PixelaUser(token=user_token, name=username)
    # To create a user, use PixelaUser function create_user, to delete a user use delete_user

    graph = GraphPixela(user_info=user, graph_id=graph_id)
    # To create a graph, use GraphPixela function create_graph
    # To add a pixel to the graph, use add_checkmark_to_graph
    # To add a pixel to specify a day, use add_another_day_checkmark_to_graph
    # To update a pixel quantity on a specific day, use update_checkmark
