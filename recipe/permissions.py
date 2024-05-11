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
