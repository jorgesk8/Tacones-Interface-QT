import os
import subprocess

def convertir_ui_a_py(archivo_ui):
    archivo_py = os.path.splitext(archivo_ui)[0] + ".py"
    
    # Cambiar a usar python -m PyQt6.uic.pyuic para la conversión
    comando_convertir = f"pyuic6 -x {archivo_ui} -o {archivo_py}"

    # Ejecutar el comando para convertir .ui a .py
    subprocess.run(comando_convertir, shell=True)

    # Manipular el contenido del archivo .py con PowerShell (si es necesario)
    comando_powershell = f"powershell -Command \"(Get-Content '{archivo_py}') -replace ':/', '' | Set-Content '{archivo_py}'\""
    subprocess.run(comando_powershell, shell=True)

if __name__ == "__main__":
    # Lista de archivos .ui que quieres convertir
    BASE_PATH = "C:\\Users\\E-PIM_15\\OneDrive - GRUPO PLASMA AUTOMATION S.A. DE C.V\\Escritorio\\TaconQT\\"
    archivos_ui = ["TaconPrincipal.ui"]

    for archivo_ui in archivos_ui:
        convertir_ui_a_py(BASE_PATH + archivo_ui)

    print("Conversión completada")
