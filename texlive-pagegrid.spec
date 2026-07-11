%global tl_name pagegrid
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Print page grid in background
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pagegrid
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagegrid.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagegrid.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagegrid.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package puts a grid on the paper. It was written for developers of
a class or package who have to put elements on definite locations on a
page (e.g. letter class). The grid allows a faster optical check,
whether the positions are correct. If the previewer already offers
features for measuring, the package might be unnecessary. Otherwise it
saves the developer from printing the page and measuring by hand. The
package was part of the oberdiek bundle.

