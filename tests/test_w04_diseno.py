from pathlib import Path
from django.conf import settings
from django.test import TestCase

BASE_DIR = Path(settings.BASE_DIR)

class DocumentosDisenioTest(TestCase):
    """Verifica existencia de artefactos de diseño del ER."""

    def test_docs_diagrama_er_existe(self):
        self.assertTrue((BASE_DIR / 'docs' / 'diagramas' / 'diagrama_er.md').exists())

    def test_diagrama_er_contiene_mermaid(self):
        path = BASE_DIR / 'docs' / 'diagramas' / 'diagrama_er.md'
        if path.exists():
            content = path.read_text(encoding='utf-8')
            self.assertIn('mermaid', content.lower())

    def test_entidades_atributos_existe(self):
        self.assertTrue((BASE_DIR / 'docs' / 'entidades_atributos.md').exists())

    def test_decisiones_diseno_existe(self):
        self.assertTrue((BASE_DIR / 'docs' / 'decisiones_diseno.md').exists())

    def test_sprint1_planning_existe(self):
        self.assertTrue((BASE_DIR / 'sprint1_planning.md').exists())