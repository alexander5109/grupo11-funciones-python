from funciones.es_primo_seling import es_primo
def test_sumar():
	assert es_primo(2) == True
	assert es_primo(15) == False
	assert es_primo(17) == True
