# revision 28986
# category Package
# catalog-ctan /macros/latex/contrib/pageslts
# catalog-date 2013-01-28 22:45:23 +0100
# catalog-license lppl1.3
# catalog-version 1.2b
Name:		texlive-pageslts
Version:	1.2b
Release:	5
Summary:	Variants of last page labels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pageslts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package was designed as an extension of the lastpage
package -- as well as that package's LastPage label (created
\AtEndDocument) it adds a VeryLastPage (created
\AfterLastShipout). When more than one page numbering scheme is
in operation (as in a book class document with frontmatter),
the labels above do not give the total number of pages, so the
package also provides labels pagesLTS.<numbering scheme>, where
the numbering scheme is arabic, roman, etc. The package relies
on the undolabl package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pageslts/pageslts.sty
%doc %{_texmfdistdir}/doc/latex/pageslts/README
%doc %{_texmfdistdir}/doc/latex/pageslts/pageslts-example.pdf
%doc %{_texmfdistdir}/doc/latex/pageslts/pageslts-example.tex
%doc %{_texmfdistdir}/doc/latex/pageslts/pageslts.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pageslts/pageslts.drv
%doc %{_texmfdistdir}/source/latex/pageslts/pageslts.dtx
%doc %{_texmfdistdir}/source/latex/pageslts/pageslts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
