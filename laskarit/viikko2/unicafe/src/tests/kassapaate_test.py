import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(5000)

    def test_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_muut(self):
        self.kassapaate.syo_edullisesti_kateisella(0)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisnosto_toimii_raha_ja_lounari_oikein_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240),0)
    
    def test_kateisnosto_toimii_raha_ja_lounari_oikein_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400),0)
    
    def test_kateisnosto_ei_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100),100)
    
    def test_kateisnosto_ei_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100),100)

    def test_korttiosto_toimii_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_korttiosto_toimii_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
    
    def test_korttiosto_ei_toimi_edullinen(self):
        self.maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_korttiosto_ei_toimi_maukas(self):
        self.maksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,50)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100050)
        self.assertEqual(self.maksukortti.saldo, 5050)

    def test_jos_lataus_nolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-50)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 5000)