%global tl_name hyphen-german
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	German hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-german
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-german.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dehyph)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for German in T1/EC and UTF-8 encodings, for
traditional and reformed spelling, including Swiss German. The package
includes the latest patterns from dehyph-exptl (known to TeX under names
'german', 'ngerman' and 'swissgerman'), however 8-bit engines still load
old versions of patterns for 'german' and 'ngerman' for backward-
compatibility reasons. Swiss German patterns are suitable for Swiss
Standard German (Hochdeutsch) not the Alemannic dialects spoken in
Switzerland (Schwyzerduetsch). There are no known patterns for written
Schwyzerduetsch.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-german:
german loadhyph-de-1901.tex
ngerman loadhyph-de-1996.tex
swissgerman loadhyph-de-ch-1901.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-german:
\addlanguage{german}{loadhyph-de-1901.tex}{}{2}{2}
\addlanguage{ngerman}{loadhyph-de-1996.tex}{}{2}{2}
\addlanguage{swissgerman}{loadhyph-de-ch-1901.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-german:
['german'] = {
	loader = 'loadhyph-de-1901.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-de-1901.pat.txt',
},
['ngerman'] = {
	loader = 'loadhyph-de-1996.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-de-1996.pat.txt',
},
['swissgerman'] = {
	loader = 'loadhyph-de-ch-1901.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-de-ch-1901.pat.txt',
},
TL_HYPHEN_EOF
