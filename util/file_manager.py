# Importo las dependencias para los datos y el manejo de archivos
import pandas as pd
import os

class CSVFileManager:
    """
    Lectura y escritura de archivos en formato CSV usando pandas
    """
    def __init__(self, ruta_archivo: str):
        """Inicializa el administrador de archivos asociándole una ruta del archivo."""
        self.ruta_archivo = ruta_archivo

    def read(self) -> pd.DataFrame:
        """
        Leeo el archivo CSV y lo convierto en dataframe. Si no existe, lanza una excepción.
        """
        if not os.path.exists(self.ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo de datos en: {self.ruta_archivo}")
        
        # Leo el archivo CSV
        return pd.read_csv(self.ruta_archivo)

    def write(self, data_frame: pd.DataFrame):
        """
        Exporta el contenido del datafraem a formato CSV en la ruta indicada.
        """
        # Se omite el índice autogenerado por Pandas tal y como se indica.
        data_frame.to_csv(self.ruta_archivo, index=False)