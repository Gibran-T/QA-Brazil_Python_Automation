import unittest
import data
import helpers


class TestUrbanRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):


        if helpers.is_reachable(data.URBAN_ROUTES_URL):

            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e em execução.")

    def setup_method(self):
        print("\nIniciando novo teste...")

    def test_set_route(self):
        # Adicionar em S8
        print("Função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Adicionar em S8
        print("Função criada para selecionar o plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("Função criada para preencher o telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("Função criada para preencher o cartão")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Função criada para adicionar comentário para o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Função criada para pedir cobertor e lenço")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            print(f"Ice cream #{count + 1} pedido")
        pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Função criada para verificar modelo de carro")
        pass

import unittest

if __name__ == "__main__":
    unittest.main()

