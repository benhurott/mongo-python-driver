
_current_session_resolver = None


def register_session_resolver(resolver):
    global _current_session_resolver
    _current_session_resolver = resolver


def resolve_session(current_session):
    global _current_session_resolver

    if not _current_session_resolver:
        return current_session

    return _current_session_resolver(current_session)
