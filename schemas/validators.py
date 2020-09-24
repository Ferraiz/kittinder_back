from controllers.build_response import build_response


def must_not_be_blank(data):
    if not data:
        raise ValidationError(build_response(
            {'error message': f'{data} not provided'}))
