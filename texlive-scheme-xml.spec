# revision 13822
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-xml
Version:	20120307
Release:	1
Summary:	XML scheme
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-xml.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-context
Requires:	texlive-jadetex
Requires:	texlive-ltxmisc
Requires:	texlive-marvosym
Requires:	texlive-metapost
Requires:	texlive-passivetex
Requires:	texlive-rotating
Requires:	texlive-stmaryrd
Requires:	texlive-tex4ht
Requires:	texlive-tipa
Requires:	texlive-ucs
Requires:	texlive-wasy
Requires:	texlive-wasysym
Requires:	texlive-xmltex
Requires:	texlive-collection-basic
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-latex
Requires:	texlive-collection-omega

%description
This contains the things you need to do XML-related work,
including PassiveTeX, JadeTeX, ConTeXt and Omega.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
