from flask import Flask, render_template, abort

app = Flask(__name__)

DISERTANTES = {
    "anibal-paz": {
        "nombre": "Dr. Aníbal Paz",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "16:00", "actividad": "Taller: Docentes — tramitación de beneficios y reclamos judiciales"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Sindicatos y regímenes especiales/diferenciales"},
        ]
    },
    "alejandra-vera": {
        "nombre": "Dra. Alejandra Vera",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "16:00", "actividad": "Taller: Docentes — tramitación de beneficios y reclamos judiciales"},
        ]
    },
    "gabriela-gonzalez": {
        "nombre": "Dra. Gabriela González",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "16:00", "actividad": "Taller: Ejecución de Sentencias — análisis de liquidación e impugnación"},
        ]
    },
    "nicolas-gattinoni": {
        "nombre": "C.PN. Nicolás Gattinoni",
        "titulo": "C.PN.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "16:00", "actividad": "Taller: Ejecución de Sentencias — análisis de liquidación e impugnación"},
        ]
    },
    "luis-criado": {
        "nombre": "Dr. Luis María Criado",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "16:00", "actividad": "Taller: Marco jurídico y reciprocidad de las cajas profesionales"},
        ]
    },
    "liliana-mathus": {
        "nombre": "Dra. Liliana Mathus",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "16:00", "actividad": "Taller: Marco jurídico y reciprocidad de las cajas profesionales"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Referente regional: Cuyo (Mendoza, San Juan y San Luis)"},
        ]
    },
    "alejandra-austerlitz": {
        "nombre": "Dra. Alejandra Austerlitz",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "18:30", "actividad": "Taller: Beneficios previsionales, judicialización y amparos"},
        ]
    },
    "carola-espin": {
        "nombre": "Dra. Carola del Pilar Espín",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "18:30", "actividad": "Taller: Beneficios previsionales, judicialización y amparos"},
            {"dia": "Jueves 25/06", "horario": "12:00 - 13:30", "actividad": "Panel I — De la litigación a la anticipación: autonomía en la vejez, protección jurídica y derecho a decidir"},
        ]
    },
    "cecilia-recalde": {
        "nombre": "Dra. Cecilia Recalde",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "18:30", "actividad": "Taller: Recurso extraordinario y queja ante la CSJN"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal Previsional — Dirección del debate"},
        ]
    },
    "adelina-loianno": {
        "nombre": "Dra. Adelina Loianno",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "18:30", "actividad": "Taller: Recurso extraordinario y queja ante la CSJN"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Marco constitucional y federal"},
        ]
    },
    "valentina-rosa": {
        "nombre": "CPN Valentina Rosa",
        "titulo": "CPN",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "18:30", "actividad": "Taller: Gestión y gobernanza de entes previsionales profesionales"},
        ]
    },
    "gustavo-beveraggi": {
        "nombre": "Arq. Gustavo Beveraggi",
        "titulo": "Arq.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "18:30", "actividad": "Taller: Gestión y gobernanza de entes previsionales profesionales"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Cajas profesionales: Autonomía, solidaridad sectorial y sustentabilidad"},
        ]
    },
    "veronica-grimaldi": {
        "nombre": "Dra. Verónica Grimaldi",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "9:30 - 11:30", "actividad": "Taller: Introducción al reajuste de haberes"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Referente regional: AMBA y Provincia de Buenos Aires"},
        ]
    },
    "carlos-salmoraghi": {
        "nombre": "Dr. Carlos Salmoraghi",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "9:30 - 11:30", "actividad": "Taller: Introducción al reajuste de haberes"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Referente regional: NOA (Salta, Jujuy, Tucumán, Santiago del Estero, La Rioja y Catamarca)"},
        ]
    },
    "rita-figueredo": {
        "nombre": "Dra. Rita Figueredo",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "9:30 - 11:30", "actividad": "Taller: Honorarios y costas en los procesos previsionales"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Referente regional: NEA (Chaco, Corrientes, Formosa y Misiones)"},
        ]
    },
    "itati-demarchi": {
        "nombre": "Dra. Itatí Demarchi",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "9:30 - 11:30", "actividad": "Taller: Honorarios y costas en los procesos previsionales"},
        ]
    },
    "paola-velarde": {
        "nombre": "Paola Velarde",
        "titulo": "",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "9:30 - 11:30", "actividad": "Taller: Comunicación estratégica en instituciones previsionales y uso de herramientas de comunicación masiva"},
        ]
    },
    "octavio-galvan": {
        "nombre": "Tec. Octavio Galván",
        "titulo": "Tec.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "9:30 - 11:30", "actividad": "Taller: Comunicación estratégica en instituciones previsionales y uso de herramientas de comunicación masiva"},
            {"dia": "Jueves 25/06", "horario": "17:30 - 19:00", "actividad": "Panel III: Inteligencia Artificial aplicada al Derecho Previsional — herramientas, automatización y gestión del conocimiento"},
        ]
    },
    "patricia-lanzon": {
        "nombre": "Esc. Patricia Lanzón",
        "titulo": "Esc.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "12:00 - 13:30", "actividad": "Panel I — Directivas anticipadas y otros instrumentos de protección en la vejez"},
        ]
    },
    "perla-goizueta": {
        "nombre": "Dra. Perla Goizueta",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "12:00 - 13:30", "actividad": "Panel I — Vivienda y decisiones de cuidado: planificación jurídica, autonomía y protección patrimonial en la vejez"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Defensa pública, discapacidad y vulnerabilidad"},
        ]
    },
    "gaston-navarro": {
        "nombre": "Dr. Gastón Navarro",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "15:00 - 17:00", "actividad": "Panel II — IA aplicada al derecho y su uso ético"},
        ]
    },
    "gabriel-chiban": {
        "nombre": "Dr. Gabriel Chiban",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "15:00 - 17:00", "actividad": "Panel II — IA y principios procesales"},
        ]
    },
    "cesar-rodriguez-galindez": {
        "nombre": "Dr. César Rodríguez Galíndez",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "15:00 - 17:00", "actividad": "Panel II — IA y congruencia en las decisiones judiciales"},
        ]
    },
    "julia-toyos": {
        "nombre": "Dra. Julia Toyos",
        "titulo": "Dra.",
        "rol": "Directora Académica",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "17:30 - 19:00", "actividad": "Panel III: Inteligencia Artificial aplicada al Derecho Previsional — herramientas, automatización y gestión del conocimiento"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Rol de la abogacía y defensa de los jubilados ante una reforma previsional"},
        ]
    },
    "juan-fantini": {
        "nombre": "Dr. Juan Fantini",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "10:00 - 12:00", "actividad": "Panel IV — Componentes del haber previsional"},
        ]
    },
    "alicia-braghini": {
        "nombre": "Dra. Alicia Braghini",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "10:00 - 12:00", "actividad": "Panel IV — Movilidad previsional y garantía constitucional: estándares jurisprudenciales y desafíos actuales"},
        ]
    },
    "elsa-rodriguez-romero": {
        "nombre": "Dra. Elsa Rodríguez Romero",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "10:00 - 12:00", "actividad": "Panel IV — La litigación previsional frente a la insuficiencia del haber: experiencia profesional, tutela efectiva y desafíos pendientes"},
        ]
    },
    "ignacio-colombo-muru": {
        "nombre": "Dr. Ignacio Colombo Murú",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "12:30 - 13:30", "actividad": "Panel V: Federalismo y Coparticipación Federal"},
        ]
    },
    "roberto-dib-ashur": {
        "nombre": "C.P.N Roberto Dib Ashur",
        "titulo": "C.P.N.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "12:30 - 13:30", "actividad": "Panel V: Federalismo y Coparticipación Federal"},
        ]
    },
    "alejandro-castellanos": {
        "nombre": "Dr. Alejandro Castellanos",
        "titulo": "Dr.",
        "rol": "Director Académico",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal Previsional — Dirección del debate"},
        ]
    },
    "silvana-ciarbonetti": {
        "nombre": "Dra. Silvana Ciarbonetti",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Sistemas provinciales: Autonomía provincial, armonización y desafíos del federalismo previsional"},
        ]
    },
    "franklin-quagliato": {
        "nombre": "Dr. Franklin Quagliato",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Régimen docente: Especialidad docente, 82% móvil y tutela constitucional"},
        ]
    },
    "ricardo-toranzos": {
        "nombre": "Dr. Ricardo Toranzos",
        "titulo": "Dr.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Régimen de magistrados y rol de los jueces ante una reforma previsional"},
        ]
    },
    "ana-britos": {
        "nombre": "Dra. Ana Britos",
        "titulo": "Dra.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Trabajadores autónomos, monotributistas, responsables inscriptos y servicio doméstico"},
        ]
    },
    "laura-cejas": {
        "nombre": "Laura Cejas",
        "titulo": "",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Referente regional: Centro (Córdoba, Santa Fe y Entre Ríos)"},
        ]
    },
    "flavia-royon": {
        "nombre": "Ing. Flavia Royón",
        "titulo": "Ing.",
        "cargo": "Senadora Nacional por Salta",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "18:45", "actividad": "El rol del Senado de la Nación en la construcción de una agenda previsional federal, sustentable y protectoria"},
        ]
    },
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cronograma')
def cronograma():
    return render_template('cronograma.html')


@app.route('/modulos_ia')
def modulos_ia():
    return render_template('modulos_ia.html')


@app.route('/disertante/<slug>')
def disertante(slug):
    speaker = DISERTANTES.get(slug)
    if not speaker:
        abort(404)
    return render_template('disertante.html', speaker=speaker, slug=slug)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
