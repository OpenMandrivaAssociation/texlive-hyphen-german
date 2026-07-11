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
Provides:	texlive(%{tl_name}) = %{tl_revision}

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

