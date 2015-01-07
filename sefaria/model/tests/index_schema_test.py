# -*- coding: utf-8 -*-

import pytest
import pprint
from sefaria.model import *

class Test_Schema(object):
    def test_schema_load(self):
        i = Index().load({"title": "Mishnah Torah Test"})
        if i:
            i.delete()
        schema = {
            "key": "Mishnah Torah Test",
            "titles": [
                {
                    "lang": "en",
                    "text": "Mishnah Torah Test",
                    "primary": True
                },
                {
                    "lang": "en",
                    "text": "Rambam Test"
                },
                {
                    "lang": "he",
                    "text": u"משנה תורה כאילו",
                    "primary": True
                }
            ],
            "nodes": [
                {
                    "key": "Introduction",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Introduction",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u"הקדמה",
                            "primary": True
                        }
                    ],
                    "nodes": [
                        {
                            "key": "Transmission",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Transmission",
                                "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "nodeParameters": {
                                "depth": 1,
                                "addressTypes": ["Integer"],
                                "sectionNames": ["Paragraph"]
                            }
                        },
                        {
                            "key": "List of Positive Mitzvot",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "List of Positive Mitzvot",
                                "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "nodeParameters": {
                                "depth": 1,
                                "addressTypes": ["Integer"],
                                "sectionNames": ["Mitzvah"]
                            }
                        },
                        {
                            "key": "List of Negative Mitzvot",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "List of Negative Mitzvot",
                                "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "nodeParameters": {
                                "depth": 1,
                                "addressTypes": ["Integer"],
                                "sectionNames": ["Mitzvah"]
                            }
                        }
                    ]

                },
                {
                    "key": "Sefer Mada",
                    "titles": [
                        {
                        "lang": "en",
                        "text": "Sefer Mada",
                        "primary": True
                        }
                    ],
                    "nodes": [
                        {
                            "key": "Foundations of the Torah",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Foundations of the Torah",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 0,
                                        "addressTypes": [],
                                        "sectionNames": []
                                    }       
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 2,
                                        "addressTypes": ["Integer", "Integer"],
                                        "sectionNames": ["Chapter", "Law"]
                                    }
                                }
                            ]
                        },
                        {
                            "key": "Human Dispositions",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Human Dispositions",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 0,
                                        "addressTypes": [],
                                        "sectionNames": []
                                    }   
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 2,
                                        "addressTypes": ["Integer", "Integer"],
                                        "sectionNames": ["Chapter", "Law"]
                                    }
                                }
                            ]
                        },
                        {
                            "key": "Torah Study",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Torah Study",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 0,
                                        "addressTypes": [],
                                        "sectionNames": []
                                    }   
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 2,
                                        "addressTypes": ["Integer", "Integer"],
                                        "sectionNames": ["Chapter", "Law"]
                                    }
                                }
                            ]
                        },
                        {
                            "key": "Foreign Worship and Customs of the Nations",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Foreign Worship and Customs of the Nations",
                                "primary": True
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 0,
                                        "addressTypes": [],
                                        "sectionNames": []
                                    }   
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 2,
                                        "addressTypes": ["Integer", "Integer"],
                                        "sectionNames": ["Chapter", "Law"]
                                    }
                                }
                            ]
                        },
                        {
                            "key": "Repentance",
                            "titles": [
                                {
                                "lang": "en",
                                "text": "Repentance",
                                "primary": True
                                },
                                {
                                "lang": "en",
                                "text": "Hilchot Teshuva",
                                "presentation": "alone"
                                }
                            ],
                            "nodes": [
                                {
                                    "key": "Introduction",
                                    "titles": [
                                        {
                                        "lang": "en",
                                        "text": "Introduction",
                                        "primary": True
                                        }
                                    ],
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 0,
                                        "addressTypes": [],
                                        "sectionNames": []
                                    }   
                                },
                                {
                                    "key": "default",
                                    "default": True,
                                    "nodeType": "JaggedArrayNode",
                                    "nodeParameters": {
                                        "depth": 2,
                                        "addressTypes": ["Integer", "Integer"],
                                        "sectionNames": ["Chapter", "Law"]
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        i = Index({
            "schema": schema,
            "title": "Mishnah Torah Test",
            "categories": ["Halakhah"]
        })
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        assert schema == i.nodes.serialize()
        i.delete()


    def test_schema_load_2(self):
        i = Index().load({"title": "Lekutei Moharan"})
        if i:
            i.delete()
        lm_schema = {
            "key": "Lekutei Moharan",
            "titles": [
                {
                    "lang": "en",
                    "text": "Lekutei Moharan",
                    "primary": True
                },
                {
                    "lang": "en",
                    "text": "Likutey Moharan"
                },
                {
                    "lang": "en",
                    "text": "Likkutei Moharan"
                },
                {
                    "lang": "he",
                    "text": u'ליקוטי מוהרן',  # took the " out from before final nun to avoid name conflict
                    "primary": True
                }
            ],
            "nodes": [
                {
                    "key": "Approbations",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Approbations",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u'הסכמות',
                            "primary": True
                        }
                    ],
                    "nodeType": "JaggedArrayNode",
                    "nodeParameters": {
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Approbation"]
                    }
                },
                {
                    "key": "Introduction",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Introduction",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u"הקדמה",
                            "primary": True
                        }
                    ],
                    "nodeType": "JaggedArrayNode",
                    "nodeParameters": {
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Paragraph"]
                    }
                },
                {
                    "key": "default",
                    "default": True,
                    "nodeType": "JaggedArrayNode",
                    "nodeParameters": {
                        "depth": 3,
                        "addressTypes": ["Integer", "Integer", "Integer"],
                        "sectionNames": ["Torah", "Section", "Paragraph"]
                    }
                },
                {
                    "key": "Tanina",
                    "titles": [
                        {
                            "lang": "en",
                            "text": "Tanina",
                            "primary": True
                        },
                        {
                            "lang": "he",
                            "text": u'תנינא',
                            "primary": True
                        }
                    ],
                    "nodes": [
                        {
                            "key": "default",
                            "default": True,
                            "nodeType": "JaggedArrayNode",
                            "nodeParameters": {
                                "depth": 3,
                                "addressTypes": ["Integer", "Integer", "Integer"],
                                "sectionNames": ["Torah", "Section", "Paragraph"]
                            }
                        },
                        {
                            "key": "Letters",
                            "titles" : [
                                {
                                    "lang": "en",
                                    "text": "Letters",
                                    "primary": True
                                },
                                {
                                    "lang": "he",
                                    "text": u'מכתב יד',
                                    "primary": True
                                }
                            ],
                            "nodeType": "JaggedArrayNode",
                            "nodeParameters": {
                                "depth": 2,
                                "addressTypes": ["Integer", "Integer"],
                                "sectionNames": ["Letter", "Paragraph"]
                            }

                        }
                    ]
                }
            ]
        }
        i = Index({
            "schema": lm_schema,
            "title": "Lekutei Moharan",
            "categories": ["Chasidut"]
        })
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        assert lm_schema == i.nodes.serialize()
        i.delete()


    def test_sharedTitles(self):
        i = Index().load({"title": "Parshanut Test"})
        if i:
            i.delete()
        schema = {
            "key": "Parshanut Test",
            "titles": [
                {
                    "lang": "en",
                    "text": "Parshanut Test",
                    "primary": True
                },
                {
                    "lang": "he",
                    "text": u'כגכג',
                    "primary": True
                }
            ],
            "nodes": [
                {
                    "key": "Bereshit",
                    "sharedTitle": "Bereshit",
                    "nodeType": "JaggedArrayNode",
                    "nodeParameters": {
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Torah"]
                    }
                },
                {
                    "key": "Noach",
                    "sharedTitle": "Noach",
                    "nodeType": "JaggedArrayNode",
                    "nodeParameters": {
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Torah"]
                    }
                },
                {
                    "key": "Lech-Lecha",
                    "sharedTitle": "Lech-Lecha",
                    "nodeType": "JaggedArrayNode",
                    "nodeParameters": {
                        "depth": 1,
                        "addressTypes": ["Integer"],
                        "sectionNames": ["Torah"]
                    }
                }
            ]
        }
        i = Index({
            "schema": schema,
            "title": "Parshanut Test",
            "categories": ["Chasidut"]
        })
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        assert schema == i.nodes.serialize()
        i.delete()

    def test_alt_struct(self):
        i = Index().load({"title": "Stest"})
        if i:
            i.delete()
        schema = {
            "key": "Stest",
            "titles": [
                {
                    "lang": "en",
                    "text": "Stest",
                    "primary": True
                },
                {
                    "lang": "he",
                    "text": u'כגככג',
                    "primary": True
                }
            ],
            "nodeType": "JaggedArrayNode",
            "nodeParameters": {
                "depth": 2,
                "addressTypes": ["Integer", "Integer"],
                "sectionNames": ["Chapter","Verse"]
            }
        }
        structs = {
            "Parasha": [
                {"sharedTitle": "Bereshit", "to": "Stest 1:1-3:4"},
                {"sharedTitle": "Noach", "to": "Stest 3:5-6:23"},
                {"sharedTitle": "Lech-Lecha", "to": "Stest 7:1-10:10"}
            ]
        }
        creating_dict = {
            "schema": schema,
            "title": "Stest",
            "categories": ["Chasidut"],
            "alt_structs": structs
        }
        i = Index(creating_dict)
        i.save()
        i.nodes.all_tree_titles("en")
        i.nodes.title_dict("en")
        assert schema == i.nodes.serialize()
        assert i.contents(support_v2=True) == creating_dict
        i.delete()



#todo : test default
