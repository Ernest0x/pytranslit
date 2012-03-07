# -*- coding: utf-8 -*-

TRANS_MAP = dict()

# Greek UN/ELOT transliteration system
TRANS_MAP['elot_743'] = {
	u'Α':	[{'replace': u'A'}],
	u'Ά':	[{'replace': u'A'}],
	u'α':	[{'replace': u'a'}],
	u'ά':	[{'replace': u'a'}],
	u'Β':	[{'replace': u'V'}],
	u'β':	[{'replace': u'v'}],
	u'Γ':	[
				{
					'after': u'ΑΆαάΒβΔδΕΈεέΖζΗΉηήΘθΙΊΪιίϊΚκΛλΜμΝνΟΌοόΠπΡρΣσςΤτΥΎΫυύϋΦφΨψΩΏωώ',
					'replace': u'G'
				},
				{
					'after': u'ΞξΧχ',
					'replace': u'N'
				},
				{
					'after': u'Γγ',
					'replace': u'N'
				},
				{
					'replace': 'G'
				}
			],
	u'γ':	[
				{
					'after': u'AΆαΒβΔδΕΈεέΖζΗΉηήΘθΙΊΪιίϊΚκΛλΜμΝνΟΌοόΠπΡρΣσςΤτΥΎΫυύϋΦφΨψΩΏωώ',
					'replace': u'g'
				},
				{
					'after': u'ΞξΧχ',
					'replace': u'n'
				},
				{
					'after': u'Γγ',
					'replace': u'n'
				},
				{
					'replace': u'g'
				}
				
			],
	u'Δ':	[{'replace': u'D'}],
	u'δ':	[{'replace': u'd'}],
	u'Ε':	[{'replace': u'E'}],
	u'Έ':	[{'replace': u'E'}],
	u'ε':	[{'replace': u'e'}],
	u'έ':	[{'replace': u'e'}],
	u'Ζ':	[{'replace': u'Z'}],
	u'ζ':	[{'replace': u'z'}],
	u'Η':	[{'replace': u'I'}],
	u'Ή':	[{'replace': u'I'}],
	u'η':	[{'replace': u'i'}],
	u'ή':	[{'replace': u'i'}],
	u'Θ':	[
				{
					'after': u'αβγδεέζηήθιίϊκλμνξοόπρστυύϋφχψωώ',
					'replace': u'Th'
				},
				{
					'replace': u'TH'
				}
			],
	u'θ':	[{'replace': u'th'}],
	u'Ι':	[{'replace': u'I'}],
	u'Ί':	[{'replace': u'I'}],
	u'Ϊ':	[{'replace': u'I'}],
	u'ι':	[{'replace': u'i'}],
	u'ί':	[{'replace': u'i'}],
	u'ϊ':	[{'replace': u'i'}],
	u'Κ':	[{'replace': u'K'}],
	u'κ':	[{'replace': u'k'}],
	u'Λ':	[{'replace': u'L'}],
	u'λ':	[{'replace': u'l'}],
	u'Μ':	[
				{
					'after': u'Ππ',
					'position': 0,
					'replace': u'B'
				},
				{
					'after': u'Ππ',
					'position': -2,
					'replace': u'B'
				},
				{
					'replace': u'M'
				}
			],
	u'μ':	[
				{
					'after': u'Ππ',
					'position': 0,
					'replace': u'b'
				},
				{
					'after': u'Ππ',
					'position': -2,
					'replace': u'b'
				},
				{
					'replace': u'm'
				}
			],
	u'Ν':	[{'replace': u'N'}],
	u'ν':	[{'replace': u'n'}],
	u'Ξ':	[{'replace': u'X'}],
	u'ξ':	[{'replace': u'x'}],
	u'Ο':	[{'replace': u'O'}],
	u'Ό':	[{'replace': u'O'}],
	u'ο':	[{'replace': u'o'}],
	u'ό':	[{'replace': u'o'}],
	u'Π':	[
				{
					'before': u'Μμ',
					'position': 1,
					'replace' : u''
				},
				{
					'before': u'Μμ',
					'position': -1,
					'replace': u''
				},
				{
					'replace': u'P'
				}
			],
	u'π':	[
				{
					'before': u'Μμ',
					'position': 1,
					'replace' : u''
				},
				{
					'before': u'Μμ',
					'position': -1,
					'replace': u''
				},
				{
					'replace': u'p'
				}
			],
	u'Ρ':	[{'replace': u'R'}],
	u'ρ':	[{'replace': u'r'}],
	u'Σ':	[{'replace': u'S'}],
	u'σ':	[{'replace': u's'}],
	u'ς':	[{'replace': u's'}],
	u'Τ':	[{'replace': u'T'}],
	u'τ':	[{'replace': u't'}],
	u'Υ':	[
				{
					'before': u'Άά',
					'replace': u'Y'
				},
				{
					'before': u'Οο',
					'replace': u'U'
				},
				{
					'before': u'Αα',
					'after': u'ΒβΓγΔδΖζΛλΜμΝνΡρΑΆαάΕΈεέΗΉηήΙΊΪιίϊΟΌοόΥΎΫυύϋΩΏωώ',
					'replace': u'V'
				},
				{
					'before': u'Αα',
					'after': u'ΘθΚκΞξΠπΣσςΤτΦφΧχΨψ',
					'replace': u'F'
				},
				{
					'before': u'Αα',
					'position': -1,
					'replace': u'F'
				},
				{
					'before': u'Έέ',
					'replace': u'Y'
				},
				{
					'before': u'Εε',
					'after': u'ΒβΓγΔδΖζΛλΜμΝνΡρΑΆαάΕΈεέΗΉηήΙΊΪιίϊΟΌοόΥΎΫυύϋΩΏωώ',
					'replace': u'V'
				},
				{
					'before': u'Εε',
					'after': u'ΘθΚκΞξΠπΣσςΤτΦφΧχΨψ',
					'replace': u'F'
				},
				{
					'before': u'Εε',
					'position': -1,
					'replace': u'F'
				},
				{
					'before': u'Ήή',
					'replace': u'Y'
				},
				{
					'before': u'Ηη',
					'after': u'ΒβΓγΔδΖζΛλΜμΝνΡρΑΆαάΕΈεέΗΉηήΙΊΪιίϊΟΌοόΥΎΫυύϋΩΏωώ',
					'replace': u'V'
				},
				{
					'before': u'Ηη',
					'after': u'ΘθΚκΞξΠπΣσςΤτΦφΧχΨψ',
					'replace': u'F'
				},
				{
					'before': u'Ηη',
					'position': -1,
					'replace': u'F'
				},
				{
					'replace': u'Y'
				}
			],
	u'Ύ':	[
				{ 
					'before': u'Οο',
					'replace': u'U'
				},
				{'replace': u'Y'}
			],
	u'Ϋ':	[{'replace': u'Y'}],
	u'υ':	[
				{
					'before': u'Άά',
					'replace': u'y'
				},
				{
					'before': u'Οο',
					'replace': u'u'
				},
				{
					'before': u'Αα',
					'after': u'ΒβΓγΔδΖζΛλΜμΝνΡρΑΆαάΕΈεέΗΉηήΙΊΪιίϊΟΌοόΥΎΫυύϋΩΏωώ',
					'replace': u'v'
				},
				{
					'before': u'Αα',
					'after': u'ΘθΚκΞξΠπΣσςΤτΦφΧχΨψ',
					'replace': u'f'
				},
				{
					'before': u'Αα',
					'position': -1,
					'replace': u'f'
				},
				{
					'before': u'Έέ',
					'replace': u'y'
				},
				{
					'before': u'Εε',
					'after': u'ΒβΓγΔδΖζΛλΜμΝνΡρΑΆαάΕΈεέΗΉηήΙΊΪιίϊΟΌοόΥΎΫυύϋΩΏωώ',
					'replace': u'v'
				},
				{
					'before': u'Εε',
					'after': u'ΘθΚκΞξΠπΣσςΤτΦφΧχΨψ',
					'replace': u'f'
				},
				{
					'before': u'Εε',
					'position': -1,
					'replace': u'f'
				},
				{
					'before': u'Ήή',
					'replace': u'y'
				},
				{
					'before': u'Ηη',
					'after': u'ΒβΓγΔδΖζΛλΜμΝνΡρΑΆαάΕΈεέΗΉηήΙΊΪιίϊΟΌοόΥΎΫυύϋΩΏωώ',
					'replace': u'v'
				},
				{
					'before': u'Ηη',
					'after': u'ΘθΚκΞξΠπΣσςΤτΦφΧχΨψ',
					'replace': u'f'
				},
				{
					'before': u'Ηη',
					'position': -1,
					'replace': u'f'
				},
				{
					'replace': u'y'
				}
			],
	u'ύ':	[
				{
					'before': u'Οο',
					'replace': u'u',
				},
				{'replace': u'y'}
			],
	u'ϋ':	[{'replace': u'y'}],
	u'Φ':	[{'replace': u'F'}],
	u'φ':	[{'replace': u'f'}],
	u'Χ':	[
				{
					'after': u'αβγδεέζηήθιίϊκλμνξοόπρστυύϋφχψωώ',
					'replace': u'Ch'
				},
				{
					'replace': u'CH'
				}
			],
	u'χ':	[{'replace': u'ch'}],
	u'Ψ':	[
				{
					'after': u'αβγδεέζηήθιίϊκλμνξοόπρστυύϋφχψωώ',
					'replace': u'Ps'
				},
				{
					'replace': u'PS'
				}
			],
	u'ψ':	[{'replace': u'ps'}],
	u'Ω':	[{'replace': u'O'}],
	u'Ώ':	[{'replace': u'O'}],
	u'ω':	[{'replace': u'ο'}],
	u'ώ':	[{'replace': u'ο'}]
}
