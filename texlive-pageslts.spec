%global tl_name pageslts
%global tl_revision 76054

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0g
Release:	%{tl_revision}.1
Summary:	Variants of last page labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pageslts
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pageslts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package was designed as an extension of the lastpage package -- as
well as that package's LastPage label (created in hook
enddocument/afterlastpage, formerly \AtEndDocument) it adds a
VeryLastPage (created in the same hook, but formerly \AfterLastShipout).
When more than one page numbering scheme is in operation (as in a book
class document with frontmatter), the labels above do not give the total
number of pages, so the package also provides labels pagesLTS.<numbering
scheme>, where the numbering scheme is arabic, roman, etc. The package
relies on the undolabl package. Note: The "LTS" of the package name
stands for: "L" = number of Last page, "T" = Total number of pages, "S"
= page numbering Schemes (roman, arabic, ...)

