Name:		texlive-pageslts
Version:	39164
Release:	2
Summary:	Variants of last page labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pageslts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
