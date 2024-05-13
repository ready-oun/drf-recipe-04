from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    로그인 유저는 모든 권한 가짐
    비로그인 유저는 읽기만 가능하게 권한 커스텀
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # 요청이 읽기 전용이라면
            return True  # 로그인 여부 상관없이 누구든 허용
        # 데이터 변경하는 요청은 로그인 여부 판단하여 True or False 반환
        return request.user and request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체 소유자만 수정 가능하도록 권한 커스텀
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모두에게 허용 - GET, HEAD, OPTIONS 요청 항상 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 객체 소유자에게만 부여 - 요청자(request.user)가 객체(Recipe)의 user와 동일한지 확인
        return obj.user_id == request.user
