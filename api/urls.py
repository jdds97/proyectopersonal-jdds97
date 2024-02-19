from rest_framework import routers
from .views import ClaseViewSet, ReservaViewSet, UsuarioViewSet, ClienteViewSet

app_name = "api"
router = routers.DefaultRouter()
router.register("clases", ClaseViewSet)
router.register("reservas", ReservaViewSet)
router.register("usuarios", UsuarioViewSet)
router.register("clientes", ClienteViewSet)
urlpatterns = router.urls
# endregion
