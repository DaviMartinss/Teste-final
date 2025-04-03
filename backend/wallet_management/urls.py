"""
Configuração de URL para wallet_management projeto.

Exemplos:
Visualizações de função
1. Adicionar uma importação: de my_app visualizações de importação
2. Adicione um URL aos urlpatterns: path('', views.home, name='home')
Exibições baseadas em classe
1. Adicione uma importação: de other_app.views import Home
2. Adicione uma URL aos urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
1. Importe a função include(): de django.urls import include, path
2. Adicione um URL a urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("auth/", include(("authentication.api.routers", "authentication"), "auth")),
                path("transaction/", include(("transaction.api.routers", "transaction"), "transaction")),
            ]
        ),
    ),
]
