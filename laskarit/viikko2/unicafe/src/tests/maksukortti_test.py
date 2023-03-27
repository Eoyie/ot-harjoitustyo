import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
    
    def test_saldo_vähenee_oikein_kun_rahaa(self):
        #self.maksukortti.ota_rahaa(500)
        
        self.assertTrue(self.maksukortti.ota_rahaa(500)) 
        #self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        

    def test_saldo_ei_mene_negatiiviseksi(self):
        #self.maksukortti.ota_rahaa(5000)
        
        self.assertFalse(self.maksukortti.ota_rahaa(5000))
        #self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        