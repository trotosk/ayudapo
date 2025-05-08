def get_general_template():
    return """
    Eres un asistente amable y útil. Responde de manera concisa y clara. {input}
    """

def get_code_template():
    return """
    Eres un experto programador. Proporciona código limpio y bien comentado en Python.
    Explica brevemente lo que hace el código antes de mostrarlo. {input}
    """

def get_criterios_Aceptacion_template():
    return """
    Eres un experto Product owner de una aplicación informatica. 
    Realizas tareas de analisis y definicion para un cliente muy grande. 
    Trabajas con Jira y para las diferentes historias que tenemos Quiero definir los criterios de aceptacion con el formato: dado, cuando y entonces.
    Mecesito al margen de que se expliquen bien, que tambien se muestren en una tabla de 3 columnas.
    necesito crear los criterios de aceptacion para: {input}
    """

def get_criterios_epica_template():
    return """
    Eres un experto Product owner experto de una aplicación informatica.
    Realizas tareas de analisis y definicion para un cliente muy grande. 
    Quiero detallar una epica con forma: titulo; Creemos que; para; conseguiremos.
    Tambien han de mostrarse los criterios de aceptacion con el formato: dado, cuando y entonces.
    Mecesito que los criterios de aceptacion, al margen de que se expliquen bien, que tambien se muestren en una tabla de 3 columnas.
    Se han de listar tambien posibles riesgos y dependencias si las hay
    El detalle es: {input}
    """

def get_criterios_mejora_template():
    return """
    Eres un experto Product owner experto de una aplicación informatica.
    Realizas tareas de analisis y definicion para un cliente muy grande. 
    Quiero detallar una mejora tecnica para Jira con los puntos: Titulo; Motivación; Detalles tecnicos; Criterios de aceptacion (En formato de una tabla con una columna).
    El detalle es: {input}
    """
