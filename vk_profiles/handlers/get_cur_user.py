import ast


def get_cur_user(api, log_stream):
    split = log_stream.__str__().split("\n")
    string = split[6].find("{")
    url_response = split[6][string:]
    url_response = ast.literal_eval(str(url_response))
    cur_user = api.users.get(user_ids=url_response.get("user_id"))
    return cur_user, url_response
