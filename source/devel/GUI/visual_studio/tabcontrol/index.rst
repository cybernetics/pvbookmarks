

.. index::
   pair: c♯ GUI; tabcontrol



.. _csharp_gui_tabcontrol:

=====================
c♯ GUI tab control
=====================


.. seealso::

   - http://www.dotnetperls.com/numericupdown


Un TabControl contient des pages d'onglets qui sont représentées par des objets
TabPage que vous ajoutez via la propriété TabPages.

L'ordre des pages d'onglets dans cette collection correspond à l'ordre des
onglets dans le contrôle.

L'utilisateur peut modifier le TabPage actuel en cliquant sur l'un des onglets
du contrôle.

Vous pouvez également modifier par programme le TabPage actuel en utilisant
l'une des propriétés TabControl suivantes :

- SelectedIndex
- SelectedTab

Dans Microsoft .NET Framework version 2.0, vous pouvez également utiliser l'une
des méthodes suivantes :

- SelectTab
- DeselectTab


::

    private void btn_selection_ok_Click(object sender, EventArgs e)
    {
        tabControl_VideoCell.SelectedTab = tabControl_VideoCell.TabPages[1];
    }








