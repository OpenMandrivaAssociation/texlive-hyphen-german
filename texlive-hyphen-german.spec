# revision 29725
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-german
Version:	20131012
Release:	8
Summary:	German hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-german.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for German in T1/EC and UTF-8 encodings,
for traditional and reformed spelling, including Swiss German.
The package includes the latest patterns from dehyph-exptl
(known to TeX under names 'german', 'ngerman' and
'swissgerman'), however 8-bit engines still load old versions
of patterns for 'german' and 'ngerman' for backward-
compatibility reasons. Swiss German patterns are suitable for
Swiss Standard German (Hochdeutsch) not the Alemannic dialects
spoken in Switzerland (Schwyzerduetsch). There are no known
patterns for written Schwyzerduetsch.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyphen/dehyphn.tex
%{_texmfdistdir}/tex/generic/hyphen/dehypht.tex
%{_texmfdistdir}/tex/generic/hyphen/dehyphtex.tex
%{_texmfdistdir}/tex/generic/hyphen/ghyphen.README
%_texmf_language_dat_d/hyphen-german
%_texmf_language_def_d/hyphen-german
%_texmf_language_lua_d/hyphen-german

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-german <<EOF
\%% from hyphen-german:
german loadhyph-de-1901.tex
ngerman loadhyph-de-1996.tex
swissgerman loadhyph-de-ch-1901.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-german
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-german <<EOF
\%% from hyphen-german:
\addlanguage{german}{loadhyph-de-1901.tex}{}{2}{2}
\addlanguage{ngerman}{loadhyph-de-1996.tex}{}{2}{2}
\addlanguage{swissgerman}{loadhyph-de-ch-1901.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-german
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-german <<EOF
-- from hyphen-german:
	['german'] = {
		loader = 'loadhyph-de-1901.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-de-1901.pat.txt',
		hyphenation = '',
	},
	['ngerman'] = {
		loader = 'loadhyph-de-1996.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-de-1996.pat.txt',
		hyphenation = '',
	},
	['swissgerman'] = {
		loader = 'loadhyph-de-ch-1901.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-de-ch-1901.pat.txt',
		hyphenation = '',
	},
EOF
