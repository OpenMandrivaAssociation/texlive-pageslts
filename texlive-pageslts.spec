# revision 23534
# category Package
# catalog-ctan /macros/latex/contrib/pageslts
# catalog-date 2011-08-13 08:34:58 +0200
# catalog-license lppl1.3
# catalog-version 1.2a
Name:		texlive-pageslts
Version:	1.2a
Release:	3
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
%doc %{_texmfdistdir}/source/latex/pageslts/ltxdoc.cfg
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-2
+ Revision: 754635
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-1
+ Revision: 719183
- texlive-pageslts
- texlive-pageslts
- texlive-pageslts
- texlive-pageslts

