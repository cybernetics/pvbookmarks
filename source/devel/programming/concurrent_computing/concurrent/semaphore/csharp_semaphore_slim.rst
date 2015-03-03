

.. index::
   pair: semaphore ; slim

.. _csharp_semaphore_slim:

==================================
C♯ SemaphoreSlim
==================================

.. seealso::

   - :ref:`semaphore`
   - :ref:`csharp_language`
   - http://msdn.microsoft.com/fr-fr/library/system.threading.semaphoreslim%28v=vs.100%29.aspx


.. contents::
   :depth: 3



.. versionadded:: DotNet 4.0


Introduction
=============

Alternative légère à Semaphore qui limite le nombre de threads pouvant accéder
simultanément à une ressource ou à un pool de ressources.


Proprétés de SemaphoreSlim
==========================


AvailableWaitHandle
-------------------

Retourne un WaitHandle qui peut être utilisé pour attendre sur un sémaphore.


Méthodes de SemaphoreSlim
==========================


Dispose()
----------

Libère toutes les ressources utilisées par l'instance actuelle de la classe
SemaphoreSlim.


Release()
----------

Quitte SemaphoreSlim une fois.



C♯ SemaphoreSlim.Wait()
-----------------------

Bloque le thread actuel jusqu'à ce qu'il puisse entrer dans SemaphoreSlim.


.. _csharp_sem_slim_acquire:

Wait(Int32)
-----------

.. seealso::

   - :ref:`python_sem_acquire`

Bloque le thread actuel jusqu'à ce qu'il puisse entrer dans SemaphoreSlim, à
l'aide d'un entier signé 32 bits qui spécifie le délai d'attente.

**Retourne true si le thread actuel est entré avec succès dans le SemaphoreSlim ;
sinon, false**.

Wait(CancellationToken)
-----------------------

Bloque le thread actuel jusqu'à ce qu'il puisse entrer dans SemaphoreSlim,
tout en observant un CancellationToken.


Wait(TimeSpan)
--------------

Bloque le thread actuel jusqu'à ce qu'il puisse entrer dans SemaphoreSlim, à
l'aide d'un TimeSpan pour spécifier le délai d'attente.


Wait(Int32, CancellationToken)
------------------------------

Bloque le thread actuel jusqu'à ce qu'il puisse entrer dans SemaphoreSlim, à
l'aide d'un entier signé 32 bits qui spécifie le délai d'attente, tout en
observant un CancellationToken.


Wait(TimeSpan, CancellationToken)
----------------------------------

Bloque le thread actuel jusqu'à ce qu'il puisse entrer dans SemaphoreSlim,
à l'aide d'un TimeSpan qui spécifie le délai d'attente, tout en observant un
CancellationToken.


Example
=======

::

    using System;
    using System.Threading;
    using System.Threading.Tasks;

    class SemaphoreSlimDemo
    {
        // Demonstrates:
        //      SemaphoreSlim construction
        //      SemaphoreSlim.Wait()
        //      SemaphoreSlim.Release()
        //      SemaphoreSlim.AvailableWaitHandle
        static void Main()
        {

            SemaphoreSlim ss = new SemaphoreSlim(2); // set initial count to 2
            Console.WriteLine("Constructed a SemaphoreSlim with an initial count of 2");

            Console.WriteLine("First non-blocking Wait: {0} (should be true)", ss.Wait(0));
            Console.WriteLine("Second non-blocking Wait: {0} (should be true)", ss.Wait(0));
            Console.WriteLine("Third non-blocking Wait: {0} (should be false)", ss.Wait(0));

            // Do a Release to free up a spot
            ss.Release();

            Console.WriteLine("Non-blocking Wait after Release: {0} (should be true)", ss.Wait(0));

            // Launch an asynchronous Task that releases the semaphore after 100 ms
            Task t1 = Task.Factory.StartNew(() =>
            {
                Thread.Sleep(100);
                Console.WriteLine("Task about to release SemaphoreSlim");
                ss.Release();
            });

            // You can also wait on the SemaphoreSlim via the underlying Semaphore WaitHandle.
            // HOWEVER, unlike SemaphoreSlim.Wait(), it WILL NOT decrement the count.
            // In the printout below, you will see that CurrentCount is still 1
            ss.AvailableWaitHandle.WaitOne();
            Console.WriteLine("ss.AvailableWaitHandle.WaitOne() returned, ss.CurrentCount = {0}", ss.CurrentCount);

            // Now a real Wait(), which should return immediately and decrement the count.
            ss.Wait();
            Console.WriteLine("ss.CurrentCount after ss.Wait() = {0}", ss.CurrentCount);

            // Clean up
            t1.Wait();
            ss.Dispose();
        }
    }


CancellationToken
=================


- http://msdn.microsoft.com/fr-fr/library/system.threading.cancellationtoken%28v=vs.100%29.aspx

