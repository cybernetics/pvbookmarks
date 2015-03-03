

.. index::
   pair: c♯ GUI; MessageBox



.. _csharp_gui_mesagebox:

=====================
c♯ GUI MessageBox
=====================


.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.windows.forms.messagebox.aspx


Affiche un message pouvant contenir du texte, des boutons et des symboles donnant
des informations et des instructions diverses à l'utilisateur




::

        private void btn_selection_ok_Click(object sender, EventArgs e)
        {
            int nb_selected_puits = getNbSelectedPuits();

            if (nb_selected_puits > 0)
                tabControl_VideoCell.SelectedTab = tabControl_VideoCell.TabPages[1];
            else
            {
                const string message = "Vous n'avez pas sélectionné de puits";
                const string caption = "Erreur de sélection"; ;
                MessageBox.Show(message, caption, MessageBoxButtons.OK);
            }
        }








