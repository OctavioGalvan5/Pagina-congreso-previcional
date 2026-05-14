from flask import Flask, render_template, abort

app = Flask(__name__)

DISERTANTES = {
    "anibal-paz": {
        "nombre": "Dr. Aníbal Paz",
        "titulo": "Dr.",
        "foto": "anibal-paz.png",
        "cv": "anibal-paz.pdf",
        "especializacion": "Derecho Previsional — Regímenes especiales docentes universitarios, movilidad jubilatoria y seguridad social",
        "bio": "Abogado egresado de la Universidad Nacional de Córdoba (2003), Magíster en Derecho Laboral (Universidad Blas Pascal) y Doctorando en Derecho (UBP). Director Académico de la Diplomatura en Derecho Previsional de la UNC y Co-Director de la Revista de Derecho de la Seguridad Social (Microjuris). Asesor legal de FAGDUT y gremios docentes universitarios desde 2007, con más de 100 publicaciones en la materia. Socio fundador de la Asociación Argentina de Seguridad Social y Profesor Asistente por concurso en Derecho del Trabajo y Seguridad Social (UNC, 2025). Experto evaluador CONEAU y columnista de Comercio y Justicia.",
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
        "foto": "gabriela-gonzalez.jpg",
        "cv": "gabriela-gonzalez.pdf",
        "especializacion": "Derecho de la Seguridad Social — Ejecución de sentencias, liquidación e impugnación en el fuero previsional federal",
        "bio": "Abogada egresada de la UBA (2002). Desde marzo de 2026, Secretaria II de la Corte Suprema de Justicia de la Nación (Prosecretaria administrativa). Anteriormente, Jefa de Despacho de la Sala III de la Cámara Federal de la Seguridad Social (2018–2026) y Relatora en el Juzgado Federal de 1ª Instancia de Seguridad Social N°9 (1998–2018). Docente Invitada en la Especialización en Derecho de la Seguridad Social de la Universidad Nacional de Rosario (2022–2025). Autora de publicaciones en eldial.com sobre la Ley 27.260 de Reparación Histórica.",
        "participacion": [
            {"dia": "Miércoles 24/06", "horario": "16:00", "actividad": "Taller: Ejecución de Sentencias — análisis de liquidación e impugnación"},
        ]
    },
    "nicolas-gattinoni": {
        "nombre": "C.PN. Nicolás Gattinoni",
        "titulo": "C.PN.",
        "foto": "nicolas-gattinoni.jpg",
        "cv": "nicolas-gattinoni.docx",
        "especializacion": "Pericias contables judiciales en materia previsional — Cámara Federal de la Seguridad Social",
        "bio": "Contador Público egresado de la Universidad de Buenos Aires. Diplomado en Pericias Judiciales por la Universidad Austral. Integrante del Cuerpo de Peritos Contadores Oficiales de la Corte Suprema de Justicia de la Nación, adscripto a la Cámara Federal de la Seguridad Social. Expositor en congresos de seguridad social y jornadas de derecho previsional.",
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
        "foto": "alejandra-austerlitz.jpg",
        "cv": "alejandra-austerlitz.pdf",
        "especializacion": "Derecho Internacional de la Seguridad Social — Convenios bilaterales y multilaterales, litigiosidad previsional y normativa de la seguridad social",
        "bio": "Abogada (UBA) y Licenciada en Relaciones Internacionales (Universidad de Belgrano). Ex Directora Nacional de Programación Normativa de la Secretaría de Seguridad Social (MTEySS, 2011–2018) y ex Coordinadora de Control de Litigiosidad en ANSES (2001–2010). Consultora del Banco Mundial — desarrolló el único Programa de Control de Litigiosidad de América Latina en materia de seguridad social. Negociadora de convenios bilaterales y multilaterales (MERCOSUR, Israel, Bolivia, Suiza, Canadá, Alemania, Perú, Corea). Representante argentina ante CISS, CIESS, OISS, OIT y AISS. Profesora Permanente en la Especialización en Seguridad Social (UNR) y JTP de Derecho de la Seguridad Social (UBA). Actualmente integra terna para vocal de la Cámara Federal de la Seguridad Social.",
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
        "foto": "adelina-loianno.jpg",
        "cv": "adelina-loianno.docx",
        "especializacion": "Derecho Constitucional y Derechos Humanos — Recurso extraordinario, control de constitucionalidad y derecho procesal constitucional",
        "bio": "Abogada, Procuradora y Escribana por la Facultad de Derecho de la UBA. Magíster en Justicia Constitucional y Derechos Humanos por la Universidad de Bologna (Italia). Profesora Consulta de la UBA en Derecho Constitucional y Derechos Humanos. Profesora Titular de Derechos Humanos en la Universidad Nacional de Lomas de Zamora y de Derecho Constitucional en la Universidad Abierta Interamericana. Investigadora de la Universidad de Buenos Aires. Co-Directora del Curso de Posgrado en Derecho del Arte y Legislación Cultural (UBA). Coordinadora del Seminario de Derecho Constitucional de la Facultad de Derecho UBA (2011–2022). Ex Vicepresidente de la Asociación Argentina de Derecho Procesal Constitucional.",
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
        "foto": "veronica-grimaldi.png",
        "cv": "veronica-grimaldi.pdf",
        "especializacion": "Derecho Previsional — Cajas de previsión de abogados, reajuste de haberes y seguridad social provincial",
        "bio": "Abogada con orientación en Derecho Tributario (UBA, 2001), Magíster en Dirección y Gestión de Planes y Fondos de Pensiones (OISS – Universidad de Alcalá, 2022) y Diplomada en Derecho Previsional (AABA–UBA, 2016). Titular del Estudio Jurídico Grimaldi y Asociados. Directora suplente de la Caja de la Abogacía de la Provincia de Buenos Aires (desde mayo 2024). Directora y miembro fundador del Instituto de Derecho Previsional del Colegio de Abogados de Bahía Blanca. Delegada de FACA en la Comisión de Seguridad Social (desde 2016). Integró el Consejo Directivo del Colegio de Abogados de Bahía Blanca (2014–2024).",
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
        "foto": "rita-figueredo.jpg",
        "cv": "rita-figueredo.docx",
        "especializacion": "Derecho de la Seguridad Social — Cajas de previsión profesionales, regímenes previsionales provinciales y litigación previsional en el NEA",
        "bio": "Abogada egresada de la Universidad Católica de Santa Fe, sede Posadas (1997, quinto promedio de su promoción). Magíster en Administración y Gestión de Organismos de Seguridad Social (UNAM–CIESS, México, 2012). Ejerce la profesión de forma autónoma en el área previsional desde 1997. Asesora de la Caja de Profesionales Médicos de Misiones (CAPROME) y de la Caja de Profesionales de Ciencias Económicas (CAPROCE). Consultora externa de la Caja Forense de la Provincia del Chaco. Docente universitaria en varias universidades nacionales. Representante del Colegio de Abogados de Misiones ante la Comisión de Seguridad Social de FACA. Integrante de la Comisión Jurídica de la Coordinadora de Cajas de Profesionales. Socia fundadora de APESSNEA.",
        "participacion": [
            {"dia": "Jueves 25/06", "horario": "9:30 - 11:30", "actividad": "Taller: Honorarios y costas en los procesos previsionales"},
            {"dia": "Viernes 26/06", "horario": "15:00 - 19:00", "actividad": "Debate Federal — Referente regional: NEA (Chaco, Corrientes, Formosa y Misiones)"},
        ]
    },
    "itati-demarchi": {
        "nombre": "Dra. Itatí Demarchi",
        "titulo": "Dra.",
        "foto": "itati-demarchi.jpg",
        "especializacion": "Derecho Laboral y Seguridad Social — Asesoramiento sindical, honorarios y costas en procesos previsionales",
        "bio": "Abogada litigante y asesora sindical. Presidenta del Colegio de Abogados de Villa María (Córdoba). Profesora de la UBA, Jefa de Trabajos Prácticos por concurso. Especialista en Derecho del Trabajo (UNC – UNL). Magíster en Argumentación Jurídica (Universidad Austral). Fundadora de \"Abogacía Transformadora\".",
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
        "foto": "patricia-lanzon.png",
        "cv": "patricia-lanzon.docx",
        "especializacion": "Derecho Notarial — Directivas anticipadas, autoprotección jurídica y derechos de las personas mayores",
        "bio": "Escribana titular de registro del Colegio de Escribanos de la Ciudad de Buenos Aires desde 1995 (por concurso público). Abogada egresada de la UBA. Presidenta de la Comisión de Derechos Humanos, Personalísimos y de Autoprotección del Colegio de Escribanos de CABA (desde 2017). Organizó el Registro de Actos de Autoprotección del Colegio de Escribanos de CABA desde su creación en 2007. Autora del libro \"Directivas Anticipadas\" (Di Lalla Ediciones, 2017). Magíster en Derecho de la Vejez por la Universidad Nacional de Córdoba (2026).",
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
        "foto": "gaston-navarro.jpg",
        "cv": "gaston-navarro.docx",
        "especializacion": "Derecho Procesal e Inteligencia Artificial aplicada al Derecho — Litigación civil y derecho informático",
        "bio": "Abogado litigante (UNC), Magíster en Derecho Procesal (UNR) y Doctor en Derecho (UNR). Profesor Adjunto por concurso de Derecho Procesal II en la Universidad Nacional de Catamarca. Docente de posgrados en múltiples universidades nacionales. Miembro fundador de la Comisión de Derecho Informático e Inteligencia Artificial de FACA y del Laboratorio de Derecho e IA de la Facultad de Derecho de la UNT. Actuó como Amicus Curiae de la CSJN en el caso Denegri c/ Google. Director del Instituto de Investigación y Formación Jurídica del Colegio de Abogados de Catamarca. Autor y coautor de 8 libros y 2 tratados.",
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
        "foto": "alicia-braghini.jpg",
        "cv": "alicia-braghini.docx",
        "especializacion": "Derecho Previsional — Movilidad jubilatoria, garantía constitucional del haber y gestión del proceso previsional en primera instancia",
        "bio": "Jueza Federal de 1ª Instancia en CABA, titular del Juzgado N°7 de Seguridad Social (desde noviembre 2020) y subrogante en el N°3. Abogada egresada de la UBA. Premio a la Excelencia Judicial en 2011 y 2018. Autora del «Manual de Gestión Aplicado al Proceso para la Tramitación de Causas Previsionales en Primera Instancia» (Ministerio de Justicia y DDHH de la Nación). Docente en la UBA y universidades privadas. Socia fundadora de la Asociación Argentina de Seguridad Social. Actualmente ternada para vocal en la Cámara Federal de la Seguridad Social.",
        "participacion": [
            {"dia": "Viernes 26/06", "horario": "10:00 - 12:00", "actividad": "Panel IV — Movilidad previsional y garantía constitucional: estándares jurisprudenciales y desafíos actuales"},
        ]
    },
    "elsa-rodriguez-romero": {
        "nombre": "Dra. Elsa Rodríguez Romero",
        "titulo": "Dra.",
        "foto": "elsa-rodriguez-romero.jpg",
        "cv": "elsa-rodriguez-romero.pdf",
        "especializacion": "Litigación previsional — Reajuste de haberes, tutela efectiva del jubilado y políticas de seguridad social",
        "bio": "Abogada egresada de la UBA. Titular del Estudio Jurídico Previsional Rodríguez Romero & Asociados desde 1981. Co-Directora del Curso de Posgrado de Actualización en Derecho Previsional (UBA–AABA) y Docente Estable en la Especialización en Seguridad Social (UNR). Directora del Instituto de Seguridad Social de la AABA. Ex Vicepresidente de la AABA (2015–2016). Ex Directora de la Comisión de Seguridad Social de FACA (2013–2022). Ex Consultora del PNUD (2000–2005), ex Asesora del MTEySS (2002–2007) y ex Asesora de la Cámara de Diputados de la Nación (1989–1993).",
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
